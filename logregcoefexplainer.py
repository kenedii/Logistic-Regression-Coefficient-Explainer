import numpy as np

def logodds_to_odds(change_in_logodds):
  """
  Exponentiates the change in log-odds to obtain the odds ratio, then calculates the increase in
  odds as a percentage.

  Args:
      change_in_logodds: The change in log-odds value (coefficient).

  Returns:
      The increase in odds (as a percentage)
  """

  # Convert change in log-odds to change in odds ratio.
  odds_ratio_change = np.exp(change_in_logodds)

  increase_in_odds = odds_ratio_change / (odds_ratio_change + 1) * 100

  return increase_in_odds

def explain_coefficients(model, columns, target):
  """
  Explains what the coefficients of a Logistic Regression model represent.

  Args:
      model: A scikit-learn logistic regression model
      columns: Column names for the independent variables (X) [Array]
      target: Column name for dependent variable (y) = 1 'String' (e.g. 'malignant')

  Returns:
      Dictionary containing probabilities derived from the logodds.
  """
  explanation = {}

  print(f'The logodds of all columns being zero: {model.intercept_[0]}')
  print(f'The probability of {target} with all columns == 0 is {logodds_to_odds(model.intercept_[0])}%')
  explanation[f'P({target}) | All columns = 0'] = logodds_to_odds(model.intercept_[0])/100

  for i in range(len(columns)): # Iterates through every feature in the columns array
    print(f'One unit increment in {columns[i]} will result in {model.coef_[0][i]} change in log odds.')
    print(f'One unit increment in {columns[i]} increases the probability of {target} by {logodds_to_odds(model.coef_[0][i])}%')
    explanation[f'+1 {columns[i]} increase P({target}) by'] = logodds_to_odds(model.coef_[0][i])/100

  return explanation