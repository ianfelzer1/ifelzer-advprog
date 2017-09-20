//
//  ViewController.swift
//  Stopwatch
//
//  Created by Programming on 1/18/17.
//  Copyright © 2017 Ian Felzer. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    
    @IBOutlet var timeLabel: UILabel!
    @IBOutlet var startButton: UIButton!
    @IBOutlet var stopButton:  UIButton!
    @IBOutlet var resetButton: UIButton!
    let stopwatch = Stopwatch()
    

   
    @IBAction func startButtonTapped() {
        self.stopwatch.start()
        Timer.scheduledTimer(timeInterval: 0.001, target: self, selector: #selector(ViewController.updateElapsedTimeLabel), userInfo: nil, repeats: true)
        
    }
    
    @IBAction func stopButtonTapped() {
        print(self.stopwatch.elapsedTime)
        self.stopwatch.stop()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.startButton.backgroundColor = UIColor.green
        self.startButton.layer.cornerRadius = 30
    
        self.resetButton.backgroundColor = UIColor.black
        self.resetButton.layer.cornerRadius = 30
    
        self.stopButton.backgroundColor = UIColor.red
        self.stopButton.layer.cornerRadius = 30
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    @IBAction func resetButtonTapped() {
        self.stopwatch.reset()
        self.timeLabel.text = self.stopwatch.formattedElapsedTime
    }
    func updateElapsedTimeLabel() {
        if self.stopwatch.isRunning {
          self.timeLabel.text = "\(stopwatch.formattedElapsedTime)"
        }
       
    }
}

