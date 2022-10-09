import utils
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn import svm
from sklearn import linear_model, neighbors, tree, ensemble
import csv

file = "input3.csv"
out = open("output3.csv", 'w', newline='')
writer = csv.writer(out)

prim_data = list()
utils.create_list_float(file, prim_data)
# print(prim_data)

data = list()
label = list()

utils.separate_data_label(prim_data, data, label)

train_data, test_data, train_label, test_label = \
    train_test_split(data, label, test_size=0.4, stratify=label)

# train_ratio, test_ratio = utils.check_ratio(train_label, test_label)
# print("train ratio: " + str(train_ratio))
# print("test ratio: " + str(test_ratio))


C = [.1, .5, 1, 5, 10, 50, 100]
clf = svm.SVC()
gs = GridSearchCV(clf, [{'kernel': ['linear'], 'C': C}], cv=5)
gs.fit(train_data, train_label)
best_score = gs.best_score_
test_score = gs.best_estimator_.score(test_data, test_label)
# print(best_score)
# print(test_score)
# print(gs.cv_results_['params'][gs.best_index_])
writer.writerow(['svm_linear', best_score, test_score])


C = [0.1, 1, 3]
degree = [4, 5, 6]
gamma = [0.1, 0.5]

clf = svm.SVC()
gs = GridSearchCV(clf, [{'kernel': ['poly'], 'C': C, 'gamma': gamma, 'degree': degree}], cv=5)
gs.fit(train_data, train_label)
best_score = gs.best_score_
test_score = gs.best_estimator_.score(test_data, test_label)
# print(best_score)
# print(test_score)
# print(gs.cv_results_['params'][gs.best_index_])
writer.writerow(['svm_polynomial', best_score, test_score])


C = [0.1, 0.5, 1, 5, 10, 50, 100]
gamma = [0.1, 0.5, 1, 3, 6, 10]
clf = svm.SVC()
gs = GridSearchCV(clf, [{'kernel': ['rbf'], 'C': C, 'gamma': gamma}], cv=5)
gs.fit(train_data, train_label)
best_score = gs.best_score_
test_score = gs.best_estimator_.score(test_data, test_label)
# print(best_score)
# print(test_score)
# print(gs.cv_results_['params'][gs.best_index_])
writer.writerow(['svm_rbf', best_score, test_score])


C = [0.1, 0.5, 1, 5, 10, 50, 100]
clf = linear_model.LogisticRegression()
gs = GridSearchCV(clf, [{'C': C}], cv=5)
gs.fit(train_data, train_label)
best_score = gs.best_score_
test_score = gs.best_estimator_.score(test_data, test_label)
# print(best_score)
# print(test_score)
# print(gs.cv_results_['params'][gs.best_index_])
writer.writerow(['logistic', best_score, test_score])


n_neighbors = []
leaf_size = []

for i in range(50):
    n_neighbors.append(i+1)
for i in range(5,61,5):
    leaf_size.append(i)
# print(n_neighbors)
# print(leaf_size)
clf = neighbors.KNeighborsClassifier()
gs = GridSearchCV(clf, [{'n_neighbors': n_neighbors, 'leaf_size': leaf_size}], cv=5)
gs.fit(train_data, train_label)
best_score = gs.best_score_
test_score = gs.best_estimator_.score(test_data, test_label)
# print(best_score)
# print(test_score)
# print(gs.cv_results_['params'][gs.best_index_])
writer.writerow(['knn', best_score, test_score])


max_depth = n_neighbors
min_samples_split = [2,3,4,5,6,7,8,9,10]
clf = tree.DecisionTreeClassifier()
gs = GridSearchCV(clf, [{'max_depth': max_depth, 'min_samples_split': min_samples_split}], cv=5)
gs.fit(train_data, train_label)
best_score = gs.best_score_
test_score = gs.best_estimator_.score(test_data, test_label)
# print(best_score)
# print(test_score)
# print(gs.cv_results_['params'][gs.best_index_])
writer.writerow(['decision_tree', best_score, test_score])


clf = ensemble.RandomForestClassifier()
gs = GridSearchCV(clf, [{'max_depth': max_depth, 'min_samples_split': min_samples_split}], cv=5)
gs.fit(train_data, train_label)
pbest_score = gs.best_score_
test_score = gs.best_estimator_.score(test_data, test_label)
# print(best_score)
# print(test_score)
# print(gs.cv_results_['params'][gs.best_index_])
writer.writerow(['random_forest', best_score, test_score])
out.close()

