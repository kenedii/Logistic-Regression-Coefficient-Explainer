# Logistic-Regression-Coefficient-Explainer
Explains what the coefficients of a Logistic Regression model represent in terms of log odds and probabilities. 

**def explain_coefficients(model, columns, target):**
Explains what the coefficients of a Logistic Regression model represent.

Args:

model: A scikit-learn logistic regression model

columns: Column names for the independent variables (X) [Array]

target: Column name(s) for dependent variable (y)
        - Use y=1 for binary classification 'String' (e.g. 'malignant')
        - Use array for multi-class classification 'Array' (e.g. ['setosa', 'versicolor', 'virginica'])

Returns:
      Dictionary containing probabilities derived from the logodds.

Output for breast cancer dataset:
```
The logodds of all columns being zero: 0.22088610964219466
The probability of malignant with all columns == 0 is 55.49980928735526%
One unit increment in mean radius will result in -0.3754573121827321 change in log odds.
One unit increment in mean radius increases the probability of malignant by 40.72230036653723%
One unit increment in mean texture will result in -0.3820306362927719 change in log odds.
One unit increment in mean texture increases the probability of malignant by 40.56372257939136%
One unit increment in mean perimeter will result in -0.36097104519318957 change in log odds.
One unit increment in mean perimeter increases the probability of malignant by 41.07245236232325%
One unit increment in mean area will result in -0.43946904648267593 change in log odds.
One unit increment in mean area increases the probability of malignant by 39.186749211780224%
One unit increment in mean smoothness will result in -0.16737642291383775 change in log odds.
One unit increment in mean smoothness increases the probability of malignant by 45.825330946115834%
One unit increment in mean compactness will result in 0.5607070102399454 change in log odds.
One unit increment in mean compactness increases the probability of malignant by 63.66161130215746%
One unit increment in mean concavity will result in -0.8552954644402124 change in log odds.
One unit increment in mean concavity increases the probability of malignant by 29.83231941722839%
One unit increment in mean concave points will result in -0.9628492791726085 change in log odds.
One unit increment in mean concave points increases the probability of malignant by 27.63080845415801%
One unit increment in mean symmetry will result in 0.07631245973297866 change in log odds.
One unit increment in mean symmetry increases the probability of malignant by 51.90688617262169%
One unit increment in mean fractal dimension will result in 0.32845810317254726 change in log odds.
One unit increment in mean fractal dimension increases the probability of malignant by 58.138416236498145%
One unit increment in radius error will result in -1.2892613910584563 change in log odds.
One unit increment in radius error increases the probability of malignant by 21.59778542864959%
One unit increment in texture error will result in 0.26511647777635555 change in log odds.
One unit increment in texture error increases the probability of malignant by 56.58936168162906%
One unit increment in perimeter error will result in -0.6718953978619022 change in log odds.
One unit increment in perimeter error increases the probability of malignant by 33.807255951150964%
One unit increment in area error will result in -0.9988609264065399 change in log odds.
One unit increment in area error increases the probability of malignant by 26.916543576604774%
One unit increment in smoothness error will result in -0.2795086451484248 change in log odds.
One unit increment in smoothness error increases the probability of malignant by 43.05742423629612%
One unit increment in compactness error will result in 0.7440772761354888 change in log odds.
One unit increment in compactness error increases the probability of malignant by 67.7886800075528%
One unit increment in concavity error will result in 0.10120659996290744 change in log odds.
One unit increment in concavity error increases the probability of malignant by 52.528007549455126%
One unit increment in concave points error will result in -0.32314491708681103 change in log odds.
One unit increment in concave points error increases the probability of malignant by 41.99094992438353%
One unit increment in symmetry error will result in 0.29504385901804997 change in log odds.
One unit increment in symmetry error increases the probability of malignant by 57.32305022657677%
One unit increment in fractal dimension error will result in 0.6817461599960535 change in log odds.
One unit increment in fractal dimension error increases the probability of malignant by 66.41283107285734%
One unit increment in worst radius will result in -1.0265855206892536 change in log odds.
One unit increment in worst radius increases the probability of malignant by 26.37466074859145%
One unit increment in worst texture will result in -1.3205563355653767 change in log odds.
One unit increment in worst texture increases the probability of malignant by 21.072574862862602%
One unit increment in worst perimeter will result in -0.8203966696990922 change in log odds.
One unit increment in worst perimeter increases the probability of malignant by 30.5679464412914%
One unit increment in worst area will result in -0.994671009684233 change in log odds.
One unit increment in worst area increases the probability of malignant by 26.99904536584799%
One unit increment in worst smoothness will result in -0.665715191055624 change in log odds.
One unit increment in worst smoothness increases the probability of malignant by 33.94569441350538%
One unit increment in worst compactness will result in 0.05114225449567451 change in log odds.
One unit increment in worst compactness increases the probability of malignant by 51.278277760029944%
One unit increment in worst concavity will result in -0.8802231400543129 change in log odds.
One unit increment in worst concavity increases the probability of malignant by 29.313154093897055%
One unit increment in worst concave points will result in -0.9251751648213179 change in log odds.
One unit increment in worst concave points increases the probability of malignant by 28.39045933420577%
One unit increment in worst symmetry will result in -0.8887113062614889 change in log odds.
One unit increment in worst symmetry increases the probability of malignant by 29.13758401555545%
One unit increment in worst fractal dimension will result in -0.4869903565302287 change in log odds.
One unit increment in worst fractal dimension increases the probability of malignant by 38.06028185895965%
```

**def logodds_to_odds(change_in_logodds):**
Exponentiates the change in log-odds to obtain the odds ratio, then calculates the increase in
  odds as a percentage.
  
Args:
change_in_logodds: The change in log-odds value (coefficient).

Returns:
The increase in odds (as a percentage of 100)
