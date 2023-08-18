#include <iostream>
#include <chrono>
#include <thread>

void clearScreen()
{
    // Clear the console screen
    std::cout << "\033[2J\033[1;1H";
}

void displayHeart()
{
    std::string heart =
        "    **        **  \n"
        " *******    *******\n"
        "*********  *********\n"
        " *******************\n"
        "   *************** \n"
        "     ***********   \n"
        "       *******     \n"
        "         ***       \n"
        "          *        \n";

    std::cout << heart;
}

void animateHeart()
{
    clearScreen();

    std::cout << "\n\n\n\n\n\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(300));

    for (int i = 0; i < 8; ++i)
    {
        clearScreen();
        std::cout << "\n\n\n\n\n\n";

        for (int j = 0; j < i; ++j)
            std::cout << " ";

        displayHeart();
        std::this_thread::sleep_for(std::chrono::milliseconds(300));
    }

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    clearScreen();
    std::cout << "\n\n\n\n\n\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
}

int main()
{
    std::string name;
    std::cout << "Enter your girlfriend's name: ";
    std::getline(std::cin, name);

    std::cout << "\n\n\n";
    std::cout << "Dear " << name << ",\n";
    std::cout << "You are my heart and my everything!\n";
    std::cout << "I love you with all my soul.\n\n";
    std::cout << "Yours forever,\nYour Name\n";

    animateHeart();

    return 0;
}
