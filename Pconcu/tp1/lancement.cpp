#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sys/time.h>
#include <math.h>
#include <thread>
#include <mutex>
#include <vector>

using namespace std;

double timevalsub(struct timeval *tv1, const struct timeval *tv2) {
	double res = 0;
	res = tv2->tv_sec - tv1->tv_sec;
	res += (tv2->tv_usec - tv1->tv_usec)*1.0/1000000;
	return res;
}

// Returns the duration of call
void fct(int num, int nbtours, double& results) {
	results = 0;
	struct timeval tv1, tv2;
	int err;

	printf("%d lancement de la fonction pour %d itérations\n", num, nbtours);
	// #####################################
	// Partie calcul
	double temps_total = 0;
	for (int i=0; i<nbtours; i++) {
		int j;

		err = gettimeofday(&tv1, NULL);
		if (err != 0) {
			perror("gettimeofday");
			exit(EXIT_FAILURE);
		}
		double sum = 0;
		for(j=0; j<5000000; j++) {
			sum += log(j+1);
		}

		err = gettimeofday(&tv2, NULL);
		if (err != 0) {
			perror("gettimeofday");
			exit(EXIT_FAILURE);
		}
		double duree = timevalsub(&tv1, &tv2);
		temps_total += duree;

		// Version avec "cerr" si on veut voir les problèmes
		// d'entrelacement des sorties :
		// cerr << num << " : je viens de faire un calcul dont le résultat est "
		//     << sum << ", il a fallu " << duree << " secondes" << endl ;
		// fprintf ne pose pas ce problème :
		fprintf(stdout, "%d : je viens de faire un calcul dont le résultat est %g,"
				"il a fallu %g secondes\n", num, sum, duree);
	}
	// fin de la partie calcul
	// ###########################
	results = temps_total;
	/* printf("INSIDE results %d %f\n", num, results); */
}


int main(int argc, char **argv) {
	int i;

	// Paramètres
	int nbthreads = 10;
	int nbtours = 5;

	// lecture des arguments
	if ((argc==2)&&(atoi(argv[1]))) {
		// s'il y a un argument numérique on l'utilise pour
		// connaître le nombre de threads/lancements de la fonction
		nbthreads = atoi(argv[1]);
	} else if (argc != 1) {
		// il y a au moins un argument mais qui n'est pas le bon
		cerr << "usage " << argv[0] << " [<nb de lancements et de threads>]"
			<< endl;
		exit (1);
	}
	printf("Th principal : lancement de %d fois la fonction\n", nbthreads);

	double temps_total = 0;

	//version prof:
	//creation d'un tableau de threads
	vector<thread> tab;

	// Tab pour stocker les resultats
	double results[nbthreads];

	// Lancement de threads
	for (i=0; i<nbthreads; i++){
		tab.push_back(thread(fct, i, nbtours, ref(results[i])));// results = resultat de thread mis en param par ref
		/* printf("results %d %f", i, results[i]); */
	}

	//on attends les threads
	for (i=0; i<nbthreads; i++){
		tab[i].join();
		printf("Thread %d time: %f\n", i, results[i]);
		temps_total+=results[i];
	}

	printf("Th principal : Le temps total de calcul est %f \n", temps_total);

	return 0;
}
