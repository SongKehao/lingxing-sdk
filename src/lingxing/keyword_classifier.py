# TODO: [ARCHITECTURE] This file contains business logic (classification rules) that should be in domains/lingxing/processing/. Refactor when safe.
"""
关键词规则引擎 — 混合分类方案: 规则引擎初筛(~70%) + LLM复核(~30%)
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class CoreType(StrEnum):
    """关键词核心类型"""

    CORE_BROAD = "CORE_BROAD"  # 大词，如 storage, toy, pillow
    CORE_LONGTAIL = "CORE_LONGTAIL"  # 核心长尾，如 small dog snuffle mat
    OTHER_LONGTAIL = "OTHER_LONGTAIL"  # 其他长尾词


class ClassifySource(StrEnum):
    """分类来源"""

    RULE = "RULE"  # 规则引擎
    LLM = "LLM"  # LLM 分类
    MANUAL = "MANUAL"  # 人工复核


@dataclass
class RuleClassifyResult:
    """规则引擎分类结果"""

    keyword: str
    core_type: CoreType
    source: ClassifySource
    needs_llm_review: bool  # 是否需要 LLM 复核
    attributes: dict[str, list[str]]  # 提取的属性
    confidence: float  # 置信度 0-1


# 核心品类词（通用家居/日用消费品）
CORE_CATEGORY_WORDS = {
    # 收纳类
    "storage",
    "organizer",
    "box",
    "container",
    "bag",
    "bin",
    "basket",
    "rack",
    "shelf",
    # 家纺类
    "pillow",
    "mat",
    "blanket",
    "towel",
    "sheet",
    "cushion",
    "cover",
    # 厨房类
    "bottle",
    "jar",
    "spoon",
    "fork",
    "knife",
    "cutting",
    "holder",
    # 浴室类
    "shower",
    "bath",
    "soap",
    "toothbrush",  # 宠物类
    "pet",
    "dog",
    "cat",
    "toy",
    "treat",
    "leash",
    "collar",
    # 其他
    "light",
    "lamp",
    "clock",
    "mirror",
    "hook",
    "hanger",
    "stand",
}

# 常见属性词映射
ATTRIBUTE_CATEGORIES = {
    "size": {
        "small",
        "large",
        "medium",
        "mini",
        "big",
        "tiny",
        "compact",
        "portable",
        "extra",
        "xl",
        "xxl",
        "king",
        "queen",
        "full",
        "twin",
    },
    "color": {
        "black",
        "white",
        "red",
        "blue",
        "green",
        "yellow",
        "pink",
        "purple",
        "grey",
        "gray",
        "brown",
        "orange",
        "gold",
        "silver",
        "beige",
    },
    "material": {
        "plastic",
        "wood",
        "metal",
        "cotton",
        "silk",
        "leather",
        "fabric",
        "bamboo",
        "stainless",
        "steel",
        "iron",
        "aluminum",
        "rubber",
        "silicone",
        "waterproof",
    },
    "function": {
        "foldable",
        "adjustable",
        "removable",
        "washable",
        "electric",
        "automatic",
        "manual",
        "digital",
        "smart",
        "rechargeable",
        "wireless",
        "cordless",
        "heavy",
        "duty",
        "lightweight",
    },
    "scene": {
        "kitchen",
        "bathroom",
        "bedroom",
        "living",
        "office",
        "outdoor",
        "indoor",
        "travel",
        "car",
        "home",
        "garden",
        "garage",
        "closet",
    },
    "audience": {
        "baby",
        "kids",
        "children",
        "women",
        "men",
        "elderly",
        "senior",
        "dog",
        "cat",
        "pet",
    },
}


def extract_attributes(keyword: str) -> dict[str, list[str]]:
    """
    从关键词中提取属性词

    Args:
        keyword: 关键词

    Returns:
        属性字典，如 {"material": ["plastic"], "size": ["small"]}
    """
    words = set(keyword.lower().split())
    attributes: dict[str, list[str]] = {}

    for category, category_words in ATTRIBUTE_CATEGORIES.items():
        matches = sorted(words & category_words)
        if matches:
            attributes[category] = matches

    return attributes


def classify_keyword_rule(search_term: str) -> RuleClassifyResult:
    """
    规则引擎初筛

    规则:
    1. 词长 <= 2 → CORE_BROAD (确定)
    2. 词长 >= 4 + 核心品类词 + 属性词 → CORE_LONGTAIL (确定)
    3. 词长 >= 5 → OTHER_LONGTAIL (确定)
    4. 其他 → OTHER_LONGTAIL (需要 LLM 复核)

    Args:
        search_term: 关键词

    Returns:
        RuleClassifyResult 分类结果
    """
    if not search_term or not search_term.strip():
        return RuleClassifyResult(
            keyword=search_term,
            core_type=CoreType.OTHER_LONGTAIL,
            source=ClassifySource.RULE,
            needs_llm_review=False,
            attributes={},
            confidence=0.3,
        )

    keyword = search_term.strip().lower()
    words = keyword.split()
    word_count = len(words)

    # 提取属性
    attributes = extract_attributes(keyword)

    # 规则1: 词长 <= 2 → CORE_BROAD (大词)
    if word_count <= 2:
        return RuleClassifyResult(
            keyword=search_term,
            core_type=CoreType.CORE_BROAD,
            source=ClassifySource.RULE,
            needs_llm_review=False,
            attributes=attributes,
            confidence=0.9,
        )

    # 检查是否包含核心品类词
    has_core_category = bool(set(words) & CORE_CATEGORY_WORDS)

    # 检查是否有属性词
    has_attributes = bool(attributes)

    # 规则2: 核心品类词 + 属性词 → CORE_LONGTAIL (核心长尾)
    # 设计文档: 包含核心品类词 + 属性词即可，无词长限制
    if has_core_category and has_attributes:
        return RuleClassifyResult(
            keyword=search_term,
            core_type=CoreType.CORE_LONGTAIL,
            source=ClassifySource.RULE,
            needs_llm_review=False,
            attributes=attributes,
            confidence=0.85,
        )

    # 规则3: 词长 >= 5 → OTHER_LONGTAIL (其他长尾)
    if word_count >= 5:
        return RuleClassifyResult(
            keyword=search_term,
            core_type=CoreType.OTHER_LONGTAIL,
            source=ClassifySource.RULE,
            needs_llm_review=False,
            attributes=attributes,
            confidence=0.75,
        )

    # 规则4: 其他情况 → 需要 LLM 复核
    # (词长 3-4，无明确属性或品类词)
    return RuleClassifyResult(
        keyword=search_term,
        core_type=CoreType.OTHER_LONGTAIL,
        source=ClassifySource.RULE,
        needs_llm_review=True,  # 需要 LLM 复核
        attributes=attributes,
        confidence=0.5,
    )


def batch_classify_rule(keywords: list[str]) -> tuple[list[RuleClassifyResult], list[str]]:
    """
    批量规则分类

    Args:
        keywords: 关键词列表

    Returns:
        (results, needs_llm_review)
        - results: 所有分类结果
        - needs_llm_review: 需要 LLM 复核的关键词列表
    """
    results = []
    needs_llm = []

    for kw in keywords:
        result = classify_keyword_rule(kw)
        results.append(result)
        if result.needs_llm_review:
            needs_llm.append(kw)

    return results, needs_llm


# 统计函数
def get_rule_stats(results: list[RuleClassifyResult]) -> dict:
    """
    统计规则引擎分类结果

    Returns:
        {
            "total": 100,
            "by_type": {"CORE_BROAD": 20, "CORE_LONGTAIL": 50, "OTHER_LONGTAIL": 30},
            "needs_llm_review": 15,
            "avg_confidence": 0.78
        }
    """
    total = len(results)
    if total == 0:
        return {"total": 0, "by_type": {}, "needs_llm_review": 0, "avg_confidence": 0}

    by_type: dict[str, int] = {}
    needs_llm = 0
    total_confidence = 0.0

    for r in results:
        type_key = r.core_type.value
        by_type[type_key] = by_type.get(type_key, 0) + 1
        if r.needs_llm_review:
            needs_llm += 1
        total_confidence += r.confidence

    return {
        "total": total,
        "by_type": by_type,
        "needs_llm_review": needs_llm,
        "llm_review_rate": round(needs_llm / total * 100, 1) if total > 0 else 0,
        "avg_confidence": round(total_confidence / total, 2),
    }
