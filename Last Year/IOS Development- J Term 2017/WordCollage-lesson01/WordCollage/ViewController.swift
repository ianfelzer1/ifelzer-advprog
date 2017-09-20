/*

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike
4.0 International License, by Yong Bakos.

*/

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    @IBAction func changeBackgroundColorFromSwitch(sender: UISegmentedControl)  {
        switch sender.selectedSegmentIndex {
        case 0:
        self.view.backgroundColor = UIColor.red
        case 1:
        self.view.backgroundColor = UIColor.orange
        case 2:
        self.view.backgroundColor = UIColor.yellow
        case 3:
            self.view.backgroundColor = UIColor.green
        case 4:
            self.view.backgroundColor = UIColor.blue
        default:
        break
        
        }
}
}
