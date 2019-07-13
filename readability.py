# Original version

class mysvm:
    def __init__(self,C=1.0):
        self.C=C
        self.W=0
        self.b=0
    def hingeloss (self,X,Y,W,b):
        loss=0
        loss+=0.5*np.dot(W.T,W)[0][0]
        m=X.shape[0]
        for x in range(m):
            ti=Y[x]*(np.dot(X[x].reshape(1,-1),W)+b)
            ti=ti[0]#shape W=[2,1] and X[0]=[2,]
            loss+=self.C*max(0,(1-ti))
        return loss

# Run the code through python/black
# It is easier on the eyes for your reader.  Give your code some air -- let it breathe.

class mysvm:
    def __init__(self, C=1.0):
        self.C = C
        self.W = 0
        self.b = 0

    def hingeloss(self, X, Y, W, b):
        loss = 0
        loss += 0.5 * np.dot(W.T, W)[0][0]
        m = X.shape[0]
        for x in range(m):
            ti = Y[x] * (np.dot(X[x].reshape(1, -1), W) + b)
            ti = ti[0]  # shape W=[2,1] and X[0]=[2,]
            loss += self.C * max(0, (1 - ti))
        return loss

# Commentary -- Avoid single letter variable names like the plague that they are.

class mysvm:  # Class names should be in CamelCase and should tell us what the class is all about
    def __init__(self, C=1.0):  # Does C stand for Collection, Color, Cluster?? Make it a word so your reader understands.
        self.C = C  # Uppercase is usually for contants (never change) and lowercase for variables
        self.W = 0  # Does W stand for Width, Weight, Waistline?? Make it a word so your reader understands.
        self.b = 0  # Does b stand for Bias, Boldness, Badness??  Make it a word so your reader understands.
        # This blank line is helpful for letting your reader scan your code -- pausing slightly before reading the next method.

    def hingeloss(self, X, Y, W, b):  # X and Y are probably fine but use words for W and b so we understand your intent.
        loss = 0  # Nice name!  The reader now knows what we are calculating.  But why set the variable to zero...
        loss += 0.5 * np.dot(W.T, W)[0][0]  # ...only to reset on the next line?  Why not just do it all on one line?
        m = X.shape[0]  # Does m stand for Mantissa, Matrix, Madagascar??  With a one letter name, why have this line at all?
        for x in range(m):  # Why not lose the line above and consolidate into a single line with "for x in range(X.shape[0]):"
            ti = Y[x] * (np.dot(X[x].reshape(1, -1), W) + b)  # Does ti stand for Tile, Tick, Time??  Use a word
            ti = ti[0]  # shape W=[2,1] and X[0]=[2,]  # On lines with code and comments, two spaces before # and one after.
            loss += self.C * max(0, (1 - ti))
        return loss

# Using names that help your reader to understand...

class SupportVectorMachine:
    "Use this docstring to tell your reader what this class is trying to do."
    def __init__(self, cluster=1.0):
        self.cluster = cluster
        self.weight = 0
        self.bias = 0

    def hinge_loss(self, X, Y, weight, bias):
        loss = 0.5 * np.dot(weight.T, weight)[0][0]  # explain why this make a good starting point
        for i, x in enumerate(X.shape[0]):
            tile = Y[i] * (np.dot(x.reshape(1, -1), weight) + bias)
            tile = tile[0]  # shape W=[2,1] and X[0]=[2,]
            loss += self.cluster * max(0, (1 - tile))
        return loss

