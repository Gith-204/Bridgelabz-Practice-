#Linear Regression
# import numpy as np
# import statsmodels.api as sm
# np.random.seed(0)
# X = np.random.rand(100,1)
# y = 2 + 3 * X + np.random.randn(100,1)
# X = sm.add_constant(X)
# model = sm.OLS(y,X)
# results = model.fit()
# print(results.summary()) 

#Analysis of Variance (ANOVA)
# import pandas as pd
# import numpy as np
# import statsmodels.api as sm
# import statsmodels.formula.api as smf
# np.random.seed(0)
# data = {'A': np.random.rand(30),
#         'B': np.random.rand(30),
#         'C': np.random.rand(30)} 
# df = pd.DataFrame(data)
# model = smf.ols('A ~ B + C', data=df)
# results = model.fit()
# print(results.summary()) 

#Time Series Analysis
# import numpy as np
# import statsmodels.api as sm
# import statsmodels.tsa.api as tsa
# np.random.seed(0)
# data = np.random.randn(100) + np.arange(100) * 0.5  
# model = tsa.ARIMA(data, order=(1,1,1))
# results = model.fit()
# print(results.summary()) 

#Hypothesis Testing
# import numpy as np
# import statsmodels.api as sm
# import statsmodels.stats.api as sms
# np.random.seed(0)
# X = np.random.rand(100,1)
# y = 2 + 3 * X + np.random.randn(100,1)
# X = sm.add_constant(X)
# model = sm.OLS(y,X)
# results = model.fit() 
# t_test = results.t_test([0, 1])
# print(t_test.summary()) 

#Heatmap
# import numpy as np
# import pandas as pd
# import statsmodels.graphics.correlation as sgc
# import matplotlib.pyplot as plt

# np.random.seed(0)

# data = pd.DataFrame(
#     np.random.rand(10, 10),
#     columns=[f'V{i}' for i in range(10)]
# )

# corr_matrix = data.corr().values  

# fig = sgc.plot_corr(corr_matrix, xnames=list(data.columns))

# plt.title('Statsmodels Correlation Heatmap')
# plt.tight_layout()
# plt.show()

#Chi-Square Test
# from scipy.stats import chisquare

# counts = [150, 80, 100, 70]

# n_categories = len(counts)
# total = sum(counts)
# expected = [total/n_categories] * n_categories

# chi2_stat, p_value = chisquare(
#   f_obs=counts,        
#   f_exp=expected,      
#   ddof=0              
# )

# print(f"Chi-square statistic: {chi2_stat}")
# print(f"P-value: {p_value}")

# alpha = 0.05
# if p_value < alpha:
#   print("Reject the null hypothesis: The proportions are significantly different.")
# else:
#   print("Fail to reject the null hypothesis: The proportions are not significantly different.")

#Anova LM
# import statsmodels.api as sm
# import statsmodels.formula.api as smf
# from statsmodels.stats.anova import anova_lm
# import pandas as pd
# import numpy as np

# np.random.seed(0)
# df = pd.DataFrame({'x': np.random.rand(100), 'y': np.random.rand(100)})
# df['z'] = 2 * df['x'] + df['y'] + np.random.randn(100)

# model1 = smf.ols('z ~ x', data=df).fit()
# model2 = smf.ols('z ~ x + y', data=df).fit()

# print(anova_lm(model1, model2)) 




