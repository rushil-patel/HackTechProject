//
//  LoginViewController.swift
//  HackTech
//
//  Created by Jonathan Molina on 2/27/16.
//  Copyright © 2016 Rushil Patel. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    @IBOutlet weak var passwordTextfield: UITextField!
    @IBOutlet weak var usernameTextfield: UITextField!
    
    @IBAction func loginOnClick(sender: AnyObject) {
        
        let user = "Admin"
        let pass = "password"
        let url = "https://hacktechbackend.herokuapp.com/login/"
        let request = NSMutableURLRequest(URL: NSURL(string: url)!);
        let postData = "username=\(user)&password=\(pass)"
        request.HTTPMethod = "POST";
        request.HTTPBody = postData.dataUsingEncoding(NSUTF8StringEncoding);
        
        let task = NSURLSession.sharedSession().dataTaskWithRequest(request){
            data, response, error in
            if error != nil
            {
                print("error=\(error)")
                return
            }
            print("response = \(response)")
        
            // Print out response body
            let responseString = NSString(data: data!, encoding: NSUTF8StringEncoding)
            print("responseString = \(responseString)")
        
            //Let’s convert response sent from a server side script to a NSDictionary object:
        
            let myJSON = try! NSJSONSerialization.JSONObjectWithData(data!, options: .MutableLeaves) as? NSDictionary
        
            if let parseJSON = myJSON {
                // Now we can access value of First Name by its key
                let name = parseJSON["name"] as? String
                print("firstNameValue: \(name)")
            }
        }
        
        task.resume()
        
        


    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        usernameTextfield.delegate = self
        passwordTextfield.delegate = self
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}

extension LoginViewController : UITextFieldDelegate {
    
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
    
}