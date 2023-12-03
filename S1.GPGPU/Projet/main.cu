#include <iostream>
#include <cmath>
#include <cuda_runtime.h>
#include "ppm.cpp"

// Fonction pour calculer l'angle entre deux points
__device__ float calculateAngle(float xc, float yc, float xa, float ya, float xb, float yb)
{
    return atan2f(yb - yc, xb - xc);
}

// Kernel CUDA pour le calcul de la visibilité
__global__ void naive_viewtest(const uint8_t *heightmap, int width, int height, int centerX, int centerY, uint8_t *result)
{
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < width && y < height)
    {
        float xc = x - centerX;
        float yc = y - centerY;

        for (int i = 0; i < width; i++)
        {
            for (int j = 0; j < height; j++)
            {
                float angle = calculateAngle(xc, yc, i - centerX, j - centerY);

                // Vérifiez la condition de visibilité
                if (angle < calculateAngle(xc, yc, x - centerX, y - centerY))
                {
                    // Le pixel est visible, marquez-le d'une certaine manière dans le résultat
                    result[x + y * width] = 255; // Marquez en blanc (ajustez selon vos besoins)
                }
            }
        }
    }
}

int main()
{
    // Chargez votre carte de hauteur (replacez le chemin du fichier PPM)
    los::Heightmap heightmap("Test/test_leger.ppm");

    // Obtenez les données de la carte de hauteur
    uint8_t *heightmapData = heightmap.getPtr();

    // Dimensions de la grille et du bloc
    dim3 blockSize(16, 16);
    dim3 gridSize((heightmap.getWidth() + blockSize.x - 1) / blockSize.x, (heightmap.getHeight() + blockSize.y - 1) / blockSize.y);

    // Résultat du calcul de visibilité
    uint8_t *visibilityResult = new uint8_t[heightmap.getSize()];

    // Appel du kernel CUDA
    naive_viewtest<<<gridSize, blockSize>>>(heightmapData, heightmap.getWidth(), heightmap.getHeight(), centerX, centerY, visibilityResult);

    // Attendez que tous les threads se terminent
    cudaDeviceSynchronize();

    // Sauvegardez le résultat dans un nouveau fichier PPM (replacez le chemin de sortie)
    los::Heightmap visibilityMap(heightmap.getWidth(), heightmap.getHeight());
    for (std::size_t i = 0; i < heightmap.getSize(); i++)
    {
        visibilityMap.setPixel(i % heightmap.getWidth(), i / heightmap.getWidth(), visibilityResult[i]);
    }
    visibilityMap.saveTo("/");

    // Libérez la mémoire
    delete[] visibilityResult;

    return 0;
}
