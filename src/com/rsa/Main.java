package com.rsa;

import java.util.Random;

public class Main {

    public static void main(String[] args) {
        int m = 1024;
        int n = 512;
        int k = 2024;
        int threadCount = 1;


        //Matrix initialization
        double[][] matrixA = new double[m][n];
        double[][] matrixB = new double[n][k];
        double[][] result = new double[m][k];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrixA[i][j] = Math.random();
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                matrixB[i][j] = Math.random();
            }
        }




        //Thread initialization
        Thread[] threads = new Thread[threadCount];
        for (int i = 0; i < threadCount; i++) {
            threads[i] = new Thread(new Multiplicator(i, threadCount, matrixA, matrixB, result));
        }

        //Thread execution
        final long startTime = System.currentTimeMillis();
        for (int i = 0; i < threadCount; i++) {
            threads[i].start();
        }



        //Thread joining
        try {
            for (int i = 0; i < threadCount; i++) {
                threads[i].join();
            }
        }
        catch (InterruptedException e) {
            System.out.println("Interrupted");
        }

        final long endTime = System.currentTimeMillis();
        //Result handling
//        for (int i = 0; i < m ; i++) {
//            for (int j = 0; j < k; j++) {
//                System.out.print(result[i][j] + "  ");
//            }
//            System.out.println();
//        }
        System.out.println(endTime - startTime);
    }
}
