/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package md5crypt;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;



/**
 *
 * @author abbas
 */
public class Filelookup {
    public String[] words;


    public static void main(String[] args) throws Exception {
        
       
        
    }
    public String[] method() throws MalformedURLException, IOException{
        URL oracle = new URL("https://tools.ietf.org/rfc/rfc3093.txt");
        StringBuilder build= new StringBuilder();
        String[] words;
        BufferedReader in = new BufferedReader(
        new InputStreamReader(oracle.openStream()));

        String inputLine;
        while ((inputLine = in.readLine()) != null){
            build.append(inputLine+"\n");
           // System.out.println(inputLine);
            }
        in.close();
        words = build.toString().split("\\s+");
        
        
        return words;
        
    }
    
    
}
