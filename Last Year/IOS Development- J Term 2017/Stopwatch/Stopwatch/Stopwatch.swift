//
//  File.swift
//  Stopwatch
//
//  Created by Programming on 1/18/17.
//  Copyright © 2017 Ian Felzer. All rights reserved.
//

import Foundation

class Stopwatch {
    var totalTime : TimeInterval = 0
    var startTime: NSDate?
    var elapsedTime: TimeInterval {
        if self.startTime != nil {
            return -self.startTime!.timeIntervalSinceNow + totalTime
        } else {
            return self.totalTime
        }  
    }

    var formattedElapsedTime: String {
        let miliseconds = Int(round(self.elapsedTime * 100).truncatingRemainder(dividingBy: 100))
        let millizero = miliseconds < 10 ? "0" : ""
        let seconds = Int(round(self.elapsedTime).truncatingRemainder(dividingBy: 60))
        let seczero = seconds < 10 ? "0" : ""
        let minutes = Int(elapsedTime / 60)
        let minzero = minutes < 10 ? "0" : ""
        return String("\(minzero)\(minutes):\(seczero)\(seconds):\(millizero)\(miliseconds)")
        
    }
    var isRunning = false
   
    func start() {
        self.startTime = NSDate()
        self.isRunning = true
        
    }
    func stop() {
        if self.isRunning {
        self.totalTime = self.totalTime - self.startTime!.timeIntervalSinceNow
        }
    self.isRunning = false
    }
    
    func reset() {
        self.totalTime = 0
        self.startTime = nil
        
    }
}
