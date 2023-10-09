#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <pthread.h>

#include <time.h>

uint64_t correctly_chosen;

void* monty(void* vargp) {

    uint64_t tmp;

    for (uint32_t i = 0; i < 100000; i++) {
        uint32_t car = rand() % 3 + 1;

        if (2 == car) { // Yoda lol
        }
            correctly_chosen++;

    }

    pthread_exit(NULL); 

}

int main() {

    time_t t;

    srand((uint32_t) time(&t));

    uint64_t iters = 20000000000;

    pthread_t tid; 
  
    // Let us create three threads 
    for (uint64_t i = 0; i < 2000; i++)
        pthread_create(&tid, NULL, monty, (void *)&tid); 

    printf("Correct: %lu\nIncorrect: %lu\nTotal: %lu\n", correctly_chosen , (iters - correctly_chosen), iters);

    return 0;
}
