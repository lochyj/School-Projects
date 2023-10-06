#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

#include <time.h>

typedef uint32_t chick_t;

void chick_peck(uint32_t* unpecked) {
    // Set all of the chickens to being unpecked
    chick_t* chickens = calloc(sizeof(chick_t), sizeof(chick_t) * 100);

    for (int i = 0; i < 100; i++) {
        int choice = (rand() % 2);
        int side = 0;

        int idx = i;

        switch (choice) {
            case 0:
                side = -1;
                break;
            case 1:
                side = 1;
                break;
        }

        idx = idx + side;

        if (idx > 99) {
            idx = idx - 100;
        } else if (idx < 0) {
            idx = idx + 100;
        }

        chickens[idx + side] = 1;

    }

    uint32_t up = 0;

    for (int i = 0; i < 100; i++) {
        if (chickens[i] == 0) {
            up++;
        }
    }

    // We dont want a memory leak :)
    free(chickens);

    *unpecked += up;

}

int main() {

    time_t t;

    srand((unsigned) time(&t));

    int iters = 100;

    uint32_t total = 0;

    for (int i = 0; i < iters; i++) {
        chick_peck(&total);
    }

    double percentage = (total / 100) / iters * 100;

    printf("Average pecked over %d iterations: %f\n", iters, percentage);


    return 0;
}
