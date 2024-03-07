
# Code Sample 

### Execution

#### Execution

```
        from statsmodels.tsa.api import ExponentialSmoothing
        from joblib import Parallel, delayed


        def univariate_forecast(column):
                fit1 = ExponentialSmoothing(
                        train_df[column].values[:split_point],
                        seasonal_periods=4,
                        trend="add",
                        seasonal="add",
                        use_boxcox=False,
                        initialization_method="estimated",
                ).fit()
                return fit1.forecast(10)


        split_point = int(len(train_df) * tds.train_split)
        forecasts = Parallel(n_jobs=10)(
        delayed(univariate_forecast)(column) for column in train_df.columns
)
```