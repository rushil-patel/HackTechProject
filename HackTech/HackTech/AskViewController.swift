

import UIKit

class AskViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    @IBOutlet weak var questionText: UITextView!
    @IBOutlet weak var categories: UIPickerView!
    
    var Array = ["Science", "Tech", "Social", "Other"]
    var theQuestion = ""
    var theCategorie = ""
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        categories.delegate = self
        categories.dataSource = self
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    func pickerView(pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        theCategorie = Array[row]
        return Array[row]
    }
    
    func pickerView(pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return Array.count
    }
    
    @IBAction func Asking(sender: AnyObject) {
        theQuestion = questionText.text!
        NSLog("the question was: " + theQuestion)
        NSLog("Categorie was: " + theCategorie)
    }
    
    @IBAction func CancelClick(sender: AnyObject) {
    }
    func numberOfComponentsInPickerView(pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func getQuestion()->String? {
        return theQuestion
    }
    
    func getCategorie()->String? {
        return theCategorie
    }
}