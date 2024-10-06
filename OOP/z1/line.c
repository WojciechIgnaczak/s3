#include <stdlib.h>
#include <math.h>
#include "line.h"

void line_free(line_t *l) {
    free(l);
}

point_t *line_get_start(line_t *l) {
    return l->start;
}

point_t *line_get_end(line_t *l) {
    return l->end;
}

double line_get_length(line_t *l) {
    int x1 = point_get_x(l->start);
    int y1 = point_get_y(l->start);
    int x2 = point_get_x(l->end);
    int y2 = point_get_y(l->end);

    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}
