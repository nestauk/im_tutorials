import scipy
import numpy as np
from sklearn import mixture
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity


class WrapTSNE():

    def vectors2sparse_matrix(self, vectors):
        """Transform a vector to a sparse matrix.

        Args:
            vectors (array): The set of N-dimensional vectors.

        Return:
            A sparse matrix.

        """
        return scipy.sparse.csr_matrix(vectors, dtype='double')

    def calculate_cosine_similarity(self, sparse_matrix):
        """Calculate the cosine similarity of a sparse matrix."""
        return cosine_similarity(sparse_matrix)

    def calculate_cosine_distance(self, similarities):
        """Find the cosine distance of some entities.
            Cosine distance = 1 - cosine similarity.

        Args:
            similarities (array): The cosine similarity.

        Return:
            cosine_distance (array): The cosine distance.

        """
        cos_distance = 1 - similarities
        return np.clip(cos_distance, 0, 1, cos_distance)

    def cos_dis(self, vectors):
        """Wrapper function that finds the cosine distance of given vectors.

        Args:
            vectors (array): The set of N-dimensional vectors.

        Return:
            Cosine distance.

        """
        return self.calculate_cosine_distance(self.calculate_cosine_similarity(
                                              self.vectors2sparse_matrix(
                                                vectors)))

    def reduce_dimensions(self, doc_vectors, n_iter=1500, perplexity=50):
        """Wrapper function that transforms word vectors to 2D."""
        cos_dist = self.cos_dis(doc_vectors)
        tsne = TSNE(n_components=2, random_state=0, verbose=1, n_iter=n_iter,
                    perplexity=perplexity, metric='precomputed')
        return tsne.fit_transform(cos_dist)


class GaussianMixtureEval():
    def __init__(self, data):
        self.data = data

    def fit_eval(self, max_components):
        """Evaluate GMM through BIC and keep the best model.

        Args:
            data (array): 2D space produced by t-SNE.

        Return:
            best_gmm: GMM with the lowest BIC.
            bic (array): The BIC values for the GMMs that are produced.

        """
        lowest_bic = np.infty
        bic = []
        n_components_range = range(1, max_components)
        cv_types = ['spherical', 'tied', 'diag', 'full']
        for cv_type in cv_types:
            for n_components in n_components_range:
                # Fit a Gaussian mixture model
                gmm = mixture.GaussianMixture(n_components=n_components,
                                              covariance_type=cv_type)
                gmm.fit(self.data)
                bic.append(gmm.bic(self.data))
                if bic[-1] < lowest_bic:
                    lowest_bic = bic[-1]
                    best_gmm = gmm

        bic = np.array(bic)
        return best_gmm, bic
