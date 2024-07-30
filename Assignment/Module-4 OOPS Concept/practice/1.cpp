// ovenTime returns the amount in minutes that the lasagna should stay in the
// oven.
int ovenTime() {
    // TODO: Return the correct time.
    return 40;
}

/* remainingOvenTime returns the remaining
   minutes based on the actual minutes already in the oven.
*/
int remainingOvenTime(int actualMinutesInOven) {
    // TODO: Calculate and return the remaining in the oven based on the time
    // the lasagna has already been there.
    int res;

    res = 40 - actualMinutesInOven;
    return res;
}

/* preparationTime returns an estimate of the preparation time based on the
   number of layers and the necessary time per layer.
*/
int preparationTime(int numberOfLayers) {
    // TODO: Calculate and return the preparation time with the
    // `numberOfLayers`.
    int res1 = 2 * numberOfLayers;
    return res1;
}

// elapsedTime calculates the total time spent to create and bake the lasagna so
// far.
int elapsedTime(int numberOfLayers, int actualMinutesInOven) {
    // TODO: Calculate and return the total time so far.
    int time1 = preparationTime(numberOfLayers) + actualMinutesInOven;
    return time1;
}

#include <iostream>
using namespace std;

int main() {
    int layers = 3;
    int minutesInOven = 20;

    cout << "Oven time: " << ovenTime() << " minutes" << endl;
    cout << "Remaining oven time: " << remainingOvenTime(minutesInOven) << " minutes" << endl;
    cout << "Preparation time: " << preparationTime(layers) << " minutes" << endl;
    cout << "Elapsed time: " << elapsedTime(layers, minutesInOven) << " minutes" << endl;

    return 0;
}

