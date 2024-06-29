// #include <stdio.h>
#include <stdarg.h>  // For variable arguments handling

int myprintf(const char *format, ...) {
    va_list args;
    va_start(args, format);
    
    int count = vprintf(format, args);
    
    va_end(args);
    
    return count;
}
