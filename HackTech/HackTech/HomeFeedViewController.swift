//
//  HomeFeedViewController.swift
//  HackTech
//
//  Created by Jonathan Molina on 2/27/16.
//  Copyright © 2016 Rushil Patel. All rights reserved.
//

import UIKit

class HomeFeedViewController: UITableViewController {
    @IBOutlet weak var open: UIBarButtonItem!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if self.revealViewController() != nil {
            open.target = self.revealViewController()
            open.action = Selector("revealToggle:")
            self.view.addGestureRecognizer(self.revealViewController().panGestureRecognizer())
        }
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
