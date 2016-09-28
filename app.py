################################
##  PRIMERA PRUEBA sklearn    ##
################################
#   FRUTA     PESO      TEXTURA
#   Manzana   140        1
#   Manzana   130        1
#   Pera      150        0
#   Pera      170        0


from sklearn import tree
#import sklearn

features = [[140,1],[130,1],[150,0],[170,0]]

labels = ['manzana','manzana','pera','pera']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print clf.predict([[160,0]])
