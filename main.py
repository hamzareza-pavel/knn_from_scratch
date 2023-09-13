#author: Hamza Reza Pavel
from random import seed
from csv import reader
from csv import writer
import distance_measures as dm
import processdataset as pds
import knn

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


def main():
    seed(1)
    #filename = 'breast-cancer.csv'
    filename = 'car.csv'
    #filename = 'hayes-roth.csv'

    dataset = load_csv(filename)
    lp, df = pds.process_data_set(dataset)
    n_folds = 10
    num_neighbors = 5
    scores_euc = knn.evaluate_algorithm(dataset, knn.k_nearest_neighbors, n_folds, dm.euclidean_distance, num_neighbors)
    scores_hamm = knn.evaluate_algorithm(dataset, knn.k_nearest_neighbors, n_folds, dm.hamming_distance, num_neighbors)
    scores_mann = knn.evaluate_algorithm(dataset, knn.k_nearest_neighbors, n_folds, dm.manhattan_distance, num_neighbors)
    scores_mink = knn.evaluate_algorithm(dataset, knn.k_nearest_neighbors, n_folds, dm.minkowski_distance, num_neighbors)

    print('Scores for euclidean distance: %s' % scores_euc)
    print('Mean Accuracy for euclidean distance: %.3f%%' % (sum(scores_euc)/float(len(scores_euc))))

    print('Scores for hamming distance: %s' % scores_hamm)
    print('Mean Accuracy for hamming distance: %.3f%%' % (sum(scores_hamm)/float(len(scores_hamm))))

    print('Scores for manhattan distance : %s' % scores_mann)
    print('Mean Accuracy for manhattan distance: %.3f%%' % (sum(scores_mann)/float(len(scores_mann))))

    print('Scores for minkowski distance with p=3 : %s' % scores_mink)
    print('Mean Accuracy for minkowski distance with p=3 : %.3f%%' % (sum(scores_mink)/float(len(scores_mink))))

    with open("out.csv", "w", newline="") as f:
        wrtr = writer(f)
        wrtr.writerows(dataset)

main()
