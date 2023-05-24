#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE "./input.txt"

enum { MAX_LINE_SIZE = 8 };

int sum_calories (char *curr_line, long *max_calories, int elf_cal);

void comp_cal (int *elf_cal, long *max_calories);

int sort_arr (const void* a, const void* b);

int main (void) {

        char file[] = INPUT_FILE;
        FILE *fp;
        fp = fopen(file, "r");
        long max_calories = 0;
        long cal_per_elf[300] = {0};
        if (!fp) {
                perror("Could not open file.\n");
                exit(1);
        }

         char curr_line[MAX_LINE_SIZE];
        int i = 0, nl_loc = 0, elf_cal = 0;
        while (fgets(curr_line, MAX_LINE_SIZE, fp)) {
                nl_loc = strcspn(curr_line, "\n");
                curr_line[nl_loc] = '\0';
                if (nl_loc > 1) {
                        elf_cal = sum_calories(curr_line, &max_calories, elf_cal);
                } else {
                        cal_per_elf[i] = elf_cal;
                        ++i;
                        elf_cal = 0;
                }
        }
        int arr_size = sizeof(cal_per_elf) / sizeof(long);
        printf("elfcals is %d elements\n", arr_size);

        qsort(cal_per_elf, arr_size - 1, sizeof(long), sort_arr);

        long top_3 = 0;
        for (int i = 0; i < 3; ++i) {
                top_3 += cal_per_elf[i];
        }
        printf("%ld\n", top_3);
        // printf("%ld\n", max_calories);

        // char curr_line[MAX_LINE_SIZE];
        // int i = 0, nl_loc = 0, elf_cal = 0;
        // while (fgets(curr_line, MAX_LINE_SIZE, fp)) {
        //         nl_loc = strcspn(curr_line, "\n");
        //         curr_line[nl_loc] = '\0';
        //         if (nl_loc > 1) {
        //                 elf_cal = sum_calories(curr_line, &max_calories, elf_cal);
        //         } else {
        //                 comp_cal(&elf_cal, &max_calories);
        //                 elf_cal = 0;
        //                 printf("\n");
        //         }
        // }
        // printf("%ld\n", max_calories);
}

int sum_calories (char *curr_line, long *max_calories, int elf_cal) {
        int curr_cal = atoi(curr_line);
        elf_cal += curr_cal;
        printf("%d\n", curr_cal);
        return elf_cal;
}

void comp_cal (int *elf_cal, long *max_calories) {
        if (*elf_cal > *max_calories) {
                *max_calories = *elf_cal;
        }
}

int sort_arr (const void* a, const void* b) {
        if (*(int*)a == *(int*)b) {
                return 0;
        } else {
                return *(int*)a > *(int*)b? -1: 1;
        }

}