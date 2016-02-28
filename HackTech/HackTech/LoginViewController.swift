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
        let username = usernameTextfield.text!
        let pass = passwordTextfield.text!
        
        let request = NSMutableURLRequest(URL: NSURL(string: "url here")!)
        request.HTTPMethod = "POST"
        let postString = "
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}