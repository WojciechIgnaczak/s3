#ifndef POINT_H_
#define POINT_H_

typedef struct point {
    int x;
    int y;
} point_t;

point_t* point_new(int x, int y);
void point_free(point_t* p);
int point_get_x(point_t *p);
int point_get_y(point_t *p);

#endif
