# Albion Market Calculator

AlbionMC is a Python project to calculate crafting costs of items in the game Albion Online.

# Description
AlbionMC is a handy tool for Albion Online players who want to calculate crafting costs of items and materials in the game. It analyzes available crafting recipes and determines total costs based on market prices of materials or their individual crafting costs.

# Installation  
Follow these steps to set up and install AlbionMC on your system:

1. **Docker**: Make sure you have Docker installed on your system.

2. **Clone the Repository**: Use Git to clone this repository to your computer:  
```
git clone https://github.com/jtomaspm/AlbionMC albionmc
```

3. **Navigate to the Directory**: Open a terminal and navigate to the project directory:

```
cd albionmc
```

4. **Using Ninja**:  

Build:
```
cmake -S . -B build -G Ninja -DCMAKE_MAKE_PROGRAM=ninja
```
Run:
```
ninja -C build run
```
Dev:
```
ninja -C build dev
```
Stop:
```
ninja -C build kill
```
Clear:
```
ninja -C build clear
```

5. **Using Docker-Compose**: 

Open a terminal and navigate to the apps directory:
```
cd apps
```
Run:
```
docker-compose up -d
```
Dev:
```
docker-compose up -d --build api frontend
```

# Contribution
Contributions are welcome! If you'd like to improve AlbionMC, feel free to send pull requests or open issues in the GitHub repository.

# License
This project is licensed under the MIT License.
