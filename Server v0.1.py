#!/usr/bin/env python
# coding=UTF-8
'''
Author: dofospider
since: 2021-07-27 13:05:42
lastTime: 2021-07-27 13:05:43
LastAuthor: Do not edit
'''

from requests_html import HTMLSession
import json
import logging


class Server():
    def __init__(self,
                 url=u'http://127.0.0.1',
                 serverUser='admin',
                 serverPasswd='password'):
        self.url = url
        self.serverUser = serverUser
        self.serverPasswd = serverPasswd
        self.data = {
            "name": self.serverUser,
            "pwd": self.serverPasswd,
        }
        self.se = HTMLSession()
        logging.debug("server class inited")

    def loginServer(self):

        self.cookie = self.se.post(self.url, data=self.data)
        if self.cookie.status_code == 200:
            logging.info("server logon")
            return True
            
        else:
            return False


class SuperMicroServer(Server):
    def __init__(self, url, serverUser, serverPasswd):
        super().__init__(url, serverUser, serverPasswd)

    def setFanFullSpeed(self):
        if (self.loginServer()):
            if (self.se.post('http://10.0.146.100/cgi/config_fan_mode.cgi',
                             data={"FanMode": 1}) == 200):
                logging.info("Set fan full speed successed")

    def setFanStandardSpeed(self):
        if (self.loginServer()):
            if (self.se.post('http://10.0.146.100/cgi/config_fan_mode.cgi',
                             data={"FanMode": 0}) == 200):
                logging.info("Set fan standard speed successed")


if (__name__ == '__main__'):
    LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT="%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(filename='server.log',level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

    server = SuperMicroServer('http://10.0.146.100/cgi/login.cgi', 'ADMIN',
                              'ADMIN')
    server.setFanStandardSpeed()