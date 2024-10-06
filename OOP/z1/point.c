#include <stdlib.h>
#include "point.h"

void point_free(point_t* p) {
    free(p);
}

int point_get_x(point_t *p) {
    return p->x;
}

int point_get_y(point_t *p) {
    return p->y;
}
