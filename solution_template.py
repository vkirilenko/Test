from math import log2

from torch import Tensor, sort

def num_swapped_pairs(ys_true: Tensor, ys_pred: Tensor) -> int:
    
    pass


def compute_gain(y_value: float, gain_scheme: str) -> float:
    
    pass


def dcg(ys_true: Tensor, ys_pred: Tensor, gain_scheme: str) -> float:
    count = 0
    dcg = 0
    for pred in ys_pred:
        if ys_true[pred] == 1:
            if gain_scheme == "const":
                dcg += count
            else:
                dcg += (1) / math.log2(count + 1 + 1)
        count += 1
    return dcg


def ndcg(ys_true: Tensor, ys_pred: Tensor, gain_scheme: str = 'const') -> float:
    idcg = 0
    num_item = np.sum(ys_true)
    _dcg = dsg(ys_true, ys_pred, gain_scheme = 'const')
    for i in range(num_item):
        idcg += (1) / math.log2(i + 1 + 1)
    ndcg = _dcg / idcg
    return ndcg


def precission_at_k(ys_true: Tensor, ys_pred: Tensor, k: int) -> float:
    # допишите ваш код здесь
    pass


def reciprocal_rank(ys_true: Tensor, ys_pred: Tensor) -> float:
    assert len(ys_pred) == len(ys_true)
    ranks = []
    for p, c in zip(ys_true, ys_pred):
        rank = calc_hit_rank(p, c)
        ranks.append(1.0 / rank)
    return sum(ranks) * 1.0 / len(ranks)


def p_found(ys_true: Tensor, ys_pred: Tensor, p_break: float = 0.15 ) -> float:
    pass


def average_precision(ys_true: Tensor, ys_pred: Tensor) -> float:
    actual_responses, actual_weights = zip(*ys_pred.items())
    expected_labels = [int(response in ys_true) for response in actual_responses][:top]
    actual_weights = actual_weights[:top]
    if any(expected_labels):
        score = average_precision_score(expected_labels, actual_weights)
    else:
        score = -1
    return score
