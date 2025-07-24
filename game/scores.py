import json
import os

SCORE_FILE = "high_scores.json"
MAX_SCORES = 5

def load_high_scores():
    """
    从 JSON 文件加载高分记录.
    如果文件不存在，则返回一个空列表.
    """
    if not os.path.exists(SCORE_FILE):
        return []
    try:
        with open(SCORE_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_high_scores(scores):
    """
    将高分记录保存到 JSON 文件.
    """
    with open(SCORE_FILE, 'w') as f:
        json.dump(scores, f, indent=4)

def add_score(current_score, scores):
    """
    将新分数添加到列表中，并保持列表有序且长度不超过最大值.
    """
    scores.append(current_score)
    # 从高到低排序
    scores.sort(reverse=True)
    # 只保留前 MAX_SCORES 名
    updated_scores = scores[:MAX_SCORES]
    return updated_scores
