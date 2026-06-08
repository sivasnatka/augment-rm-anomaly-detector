# Metrics calculator
from statistics import mean, pstdev

def summarize(values: list[float]) -> dict:
    if not values:
        return {'n': 0}
    return {'n': len(values), 'mean': mean(values), 'std': pstdev(values)}
