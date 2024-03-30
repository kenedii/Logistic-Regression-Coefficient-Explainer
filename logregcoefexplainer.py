import numpy as np

def logodds_to_odds(change_in_logodds):
  """
  Exponentiates the change in log-odds to obtain the odds ratio, then calculates the increase in
  odds as a percentage.

  Args:
      change_in_logodds: The change in log-odds value (coefficient).

  Returns:
      The increase in odds (as a percentage of 100)
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
      target: Column name(s) for dependent variable (y)
        - Use y=1 for binary classification 'String' (e.g. 'malignant')
        - Use array for multi-class classification 'Array' (e.g. ['setosa', 'versicolor', 'virginica'])

  Returns:
      Dictionary containing probabilities derived from the logodds.
  """
  explanation = {}

  if len(model.intercept_) == 1: # For Binary Classification

    if len(columns) == 1: # Only one independent variable (X)
      print(f'The logodds of {columns[0]} being zero: {model.intercept_[0]}')
      print(f'The probability of {target} with {columns[0]} = 0 is {logodds_to_odds(model.intercept_[0])}%')

      explanation[f'P({target}) | {columns[0]} = 0'] = logodds_to_odds(model.intercept_[0])/100

      print(f'One unit increment in {columns[0]} will result in {model.coef_[0][0]} change in log odds.')
      print(f'One unit increment in {columns[0]} increases the probability of {target} by {logodds_to_odds(model.coef_[0][0])}%')

      explanation[f'+1 {columns[0]} increase P({target}) by'] = logodds_to_odds(model.coef_[0][i])/100
      return explanation

    if len(columns) > 1: # Multiple independent variables
      print(f'The logodds of all columns being zero: {model.intercept_[0]}')
      print(f'The probability of {target} with all columns == 0 is {logodds_to_odds(model.intercept_[0])}%')
      explanation[f'P({target}) | All columns = 0'] = logodds_to_odds(model.intercept_[0])/100

      for i in range(len(columns)): # Iterates through every feature in the columns array
        print(f'One unit increment in {columns[i]} will result in {model.coef_[0][i]} change in log odds.')
        print(f'One unit increment in {columns[i]} increases the probability of {target} by {logodds_to_odds(model.coef_[0][i])}%')
        explanation[f'+1 {columns[i]} increase P({target}) by'] = logodds_to_odds(model.coef_[0][i])/100

      return explanation
    
  if len(model.intercept_) > 1: # Multi-class Classification

    if len(columns) == 1: # Only one independent variable (X)
      for i in range(len(target)): # Iterate through each target class
        print(f'The logodds of {columns[0]} being zero for {target[i]}: {model.intercept_[i]}')
        print(f'The probability of {target[i]} with {columns[0]} = 0 is {logodds_to_odds(model.intercept_[i])}%')

        explanation[f'P({target[i]}) | {columns[0]} = 0'] = logodds_to_odds(model.intercept_[i])/100

        for j in range(len(columns)): # Iterate through each feature in the columns array
          print(f'One unit increment in {columns[0]} will result in {model.coef_[i][j]} change in log oddsfor {target[i]}.')
          print(f'One unit increment in {columns[0]} increases the probability of {target[i]} by {logodds_to_odds(model.coef_[i][j])}%')

          explanation[f'+1 {columns[0]} increase P({target}) by'] = logodds_to_odds(model.coef_[i][j])/100
      
      return explanation
    
    if len(columns) > 1: # Multiple independent variables
      for i in range(len(target)): # Iterate through each target class
        print(f'The logodds of {columns[0]} being zero for {target[i]}: {model.intercept_[i]}')
        print(f'The probability of {target[i]} with all columns = 0 is {logodds_to_odds(model.intercept_[i])}%')

        explanation[f'P({target[i]}) | {columns[0]} = 0'] = logodds_to_odds(model.intercept_[i])/100

        for j in range(len(columns)): # Iterate through each feature in the columns array
          print(f'One unit increment in {columns[0]} will result in {model.coef_[i][j]} change in log odds for {target[i]}.')
          print(f'One unit increment in {columns[0]} increases the probability of {target[i]} by {logodds_to_odds(model.coef_[i][j])}%')

          explanation[f'+1 {columns[0]} increase P({target[i]}) by'] = logodds_to_odds(model.coef_[i][j])/100
      
      return explanation

