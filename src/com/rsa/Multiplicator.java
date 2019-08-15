package com.rsa;

import java.util.Random;

public class Multiplicator implements Runnable {
    private int part;
    private int totalParts;
    private double [][] result;
    private double[][] matrixA;
    private double[][] matrixB;

    public Multiplicator(int part, int totalParts, double[][] matrixA, double [][] matrixB, double[][] result) {
        this.part = part;
        this.totalParts = totalParts;
        this.matrixA = matrixA;
        this.matrixB = matrixB;
        this.result = result;
    }

    @Override
    public void run() {
        int totalRows = matrixA.length;
        int totalColumns = matrixB[0].length;
        for (int i = part * totalRows / totalParts; i < (part + 1) * totalRows / totalParts; i++) {
            for (int j = 0; j < totalColumns; j++) {
                for (int k = 0; k < matrixA[0].length; k++) {
                    result[i][j] += matrixA[i][k] + matrixB[k][j];
                }
            }

        }
    }
}
