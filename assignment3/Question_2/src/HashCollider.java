/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.math.BigInteger;
import java.util.Random;
import org.apache.commons.codec.digest.DigestUtils;

/**
 *
 * @author abbas
 */
public class HashCollider {

    /**i
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Random random = new Random();
        byte[] nbytes1 = new byte[64];
        byte[] nbytes2 = new byte[64];
        float average=0;
        // set number of bits for checking collision
        int number_of_bits=4;
        random.nextBytes(nbytes1);
        random.nextBytes(nbytes2);

        String sha1=DigestUtils.sha256Hex(nbytes1);
        String sha2=DigestUtils.sha256Hex(nbytes2);

        String nsh1=new BigInteger(sha1, 16).toString(2);
        String nsh2=new BigInteger(sha2, 16).toString(2);
        int i=0;
        for(int j=0;j<5;j++){
        while(true){
            if(nsh1.substring(0,number_of_bits-1).equals(nsh2.substring(0,number_of_bits-1))){
            System.out.println(i);
             average +=i;
              break;
            }
            i++;
//            System.out.println("......"+i);
            random.nextBytes(nbytes1);
            random.nextBytes(nbytes2);
            sha1=DigestUtils.sha256Hex(nbytes1);
            sha2=DigestUtils.sha256Hex(nbytes2);
            nsh1=new BigInteger(sha1, 16).toString(2);
            nsh2=new BigInteger(sha2, 16).toString(2);
        }
        i=0;
//        System.out.println(nsh1+"\n"+nsh2);
        random.nextBytes(nbytes1);
        random.nextBytes(nbytes2);
        sha1=DigestUtils.sha256Hex(nbytes1);
        sha2=DigestUtils.sha256Hex(nbytes2);
        nsh1=new BigInteger(sha1, 16).toString(2);
        nsh2=new BigInteger(sha2, 16).toString(2);


        }
        //
        System.out.println("Average for  "+number_of_bits+ " bits is  "+average/5);


    }

}
