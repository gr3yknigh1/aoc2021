#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctype.h>


int main()
{
    std::ifstream file("input.txt");
    std::string input;
    if (file.is_open())
    {
        std::getline(file, input);
    }
    file.close();

    int day_count = 256;
    int newborn_initial_value = 8;
    int value_after_breed = 6;

    std::vector<int> fishes;
    std::vector<int> newborn;

    for (int i = 0; i <= input.size(); i++)
    {
        if (!isdigit(input[i])) continue;
        int f = (int)input[i] - 48;
        fishes.push_back(f);
    }


    for (int d = 0; d < day_count; d++)
    {
        for (int i = 0; i < fishes.size(); i++)
        {
            if (fishes[i] == 0)
            {
                fishes[i] = value_after_breed;
                newborn.push_back(newborn_initial_value);
                continue;
            }
            fishes[i]--;
        }

        for (int y = 0; y < newborn.size(); y++)
        {
            fishes.push_back(newborn[y]);
        }
        newborn.clear();
    }

    std::cout << "Total: " << fishes.size() << std::endl;

    return 0;
}