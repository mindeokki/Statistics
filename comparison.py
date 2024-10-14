import matplotlib.pyplot as plt
from scipy.stats import ttest_rel, mannwhitneyu

# Example data: performance metrics (e.g., accuracies) from two models
model1_performance = [0.85, 0.87, 0.83, 0.88, 0.86]
model2_performance = [0.82, 0.84, 0.81, 0.85, 0.83]

plt.boxplot(model1_performance)
plt.boxplot(model2_performance)
plt.show()


def do_ttest(list1, list2):  # When 정규집단 만족
    t_statistic, p_value = ttest_rel(list1, list2)
    return t_statistic, p_value


def do_mannwhitneyu(list1, list2, alternative='greater'):  # When 정규집단 불만족
    u_statistic, p_value = mannwhitneyu(model1_performance, model2_performance,
                                        alternative='greater')  # model1 performance greater than model2 performance
    return u_statistic, p_value


# Perform paired t-test
# t_statistic, p_value = ttest_rel(model1_performance, model2_performance)

# print(f"Paired t-test p-value: {p_value}")

u_statistic, p_value = do_mannwhitneyu(model1_performance, model2_performance, alternative='greater')

print(f"Mann-Whitney U test statistic: {u_statistic}")
print(f"Mann-Whitney U test p-value: {p_value}")
