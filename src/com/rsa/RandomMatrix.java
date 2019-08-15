package com.rsa;

import java.util.concurrent.ThreadLocalRandom;

public class RandomMatrix {
    public int m;
    public int n;

    public double[][] matrix;

    public RandomMatrix(int m, int n) {
        this.m = m;
        this.n = n;

        matrix = new double[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Math.random();
            }
        }
    }
}
