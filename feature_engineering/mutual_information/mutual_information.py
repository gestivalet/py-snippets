#----------------------------------------------#
#------------- Mutual Information -------------#
#----------------------------------------------#

# Goal: Locate features with the most potential



#-------- SCIKIT-LEARN implementation ---------#
# Scikit-learn has two mutual information metrics in its feature_selection module:
# - one for real-valued targets (mutual_info_regression)
# - one for categorical targets (mutual_info_classif).

from sklearn.feature_selection import mutual_info_regression, mutual_info_classif



#-------------- Compute MI --------------------#

X = df.copy()
y = X.pop("price") # 'price' is target


#--- step1: preprocess
# Label encoding for categoricals
for colname in X.select_dtypes("object"):
    X[colname], _ = X[colname].factorize()


#--- step2: get a list of all discrete features (no matter if regression/classif)
# All discrete features should now have integer dtypes (double-check this before using MI!)
discrete_features = X.dtypes == int # the others should be float in this example


#--- step3: compute MI
def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores

mi_scores = make_mi_scores(X, y, discrete_features)
mi_scores[::3]  # show a few features with their MI scores  ~  .head(x)


#--- step4: visualize results
def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")

plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores)


#--- step5: sanity-check (check feats with highest/lowest MI)
# check feat with highest MI vs. target
sns.relplot(x="curb_weight", y="price", data=df);

# shows how the feat with lowest MI score relates (or actually does not relate) to target
sns.lmplot(x="horsepower", y="price", hue="fuel_type", data=df); # plots multiple-regression lines