
import UIKit

class AnswerViewController: UIViewController {
    
    @IBOutlet weak var question: UITextView!
    @IBOutlet weak var answer: UITextView!
    
    var theQuestion = "how to promgram in swift?"
    var theAnswer = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    @IBAction func submitClick(sender: AnyObject) {
        self.getAnswer()
        NSLog("the answer was: " + theAnswer)
        
    }
    
    @IBAction func cancelClick(sender: AnyObject) {
    }
    
    func getAnswer()->String? {
        theAnswer = answer.text
        return theAnswer
    }
}