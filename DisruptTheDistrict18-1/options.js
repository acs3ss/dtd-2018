window.addEventListener('DOMContentLoaded', function() {var link = document.getElementById('btnOpenNewTab0');link.addEventListener('click', function() {var newURL = "http://guns.news/";chrome.tabs.create({ url: newURL });});var link = document.getElementById('btnOpenNewTab1');link.addEventListener('click', function() {var newURL = "http://abcnews.go.com/US/guns-/story?id=53388007";chrome.tabs.create({ url: newURL });});var link = document.getElementById('btnOpenNewTab2');link.addEventListener('click', function() {var newURL = "https://www.vox.com/policy-and-politics/2018/3/2/17050610/guns-shootings-studies-rand-charts-maps";chrome.tabs.create({ url: newURL });});var link = document.getElementById('btnOpenNewTab3');link.addEventListener('click', function() {var newURL = "https://www.nytimes.com/2018/02/28/us/politics/trump-gun-control.html";chrome.tabs.create({ url: newURL });});var link = document.getElementById('btnOpenNewTab4');link.addEventListener('click', function() {var newURL = "http://www.guns.com/";chrome.tabs.create({ url: newURL });});});