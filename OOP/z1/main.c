#include <stdio.h>
#include <stdlib.h>
#include "line.h"
#include "Point.h"

int main() {
    point_t *p1 = point_new(10, 20);
    if (!p1) {
        printf("Błąd alokacji pamięci dla p1\n");
        return 1;
    }

    point_t *p2 = point_new(30, 40);
    if (!p2) {
        printf("Błąd alokacji pamięci dla p2\n");
        point_free(p1);
        return 1;
    }

    line_t *l1 = line_new(p1, p2);
    if (!l1) {
        printf("Błąd alokacji pamięci dla linii\n");
        point_free(p1);
        point_free(p2);
        return 1;
    }

    printf("Długość linii: %f\n", line_get_length(l1));

    line_free(l1);
    point_free(p2);
    point_free(p1);

    return 0;
}

point_t *point_new(int x, int y) {
    point_t *p = malloc(sizeof(point_t));
    if (!p) {
        return NULL;
    }
    p->x = x;
    p->y = y;
    return p;
}

line_t *line_new(point_t *p1, point_t *p2) {
    line_t *l = malloc(sizeof(line_t));
    if (!l) {
        return NULL;
    }
    l->start = p1;
    l->end = p2;
    return l;
}
