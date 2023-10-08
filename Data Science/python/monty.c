#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

#include <time.h>

void monty(uint64_t* correctly_chosen) {

    int your_choice = (rand() % 3);

    int car = (rand() % 3);

    if (your_choice == car) {
        *correctly_chosen += 1;
    }

    return;

}

int main() {

    time_t t;

    srand((unsigned) time(&t));

    uint64_t iters = 1000000000;

    uint64_t total = 0;

    for (uint64_t i = 0; i < iters; i++) {
        monty(&total);
    }

    printf("Correct: %lu\nIncorrect: %lu\n", total , (iters - total) );

    return 0;
}
