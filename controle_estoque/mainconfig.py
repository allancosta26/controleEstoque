# -*- coding: utf-8 -*-
import configparser
import os
import sys


from Views.mainConfig import Ui_ct_MainConfig
from mainempresa import MainEmpresa
from maindbconf import MainDbConf


from orm.CrudEmpresa import CrudEmpresa


class MainConfig(Ui_ct_MainConfig, MainEmpresa, MainDbConf):

    def mainconfig(self, frame):
        super(MainConfig, self).setMainConfig(frame)
        self.frameMainConfig.show()

        # Abrindo janela Empresa como primeira janela
        self.janelaConfEmpresa()

        # Botao Empresa
        self.bt_confEmpresa.clicked.connect(self.janelaConfEmpresa)

        # Botao Bando de dados
        self.bt_confDB.clicked.connect(self.janelaDbConf)

    # janela Dados empresa
    def janelaConfEmpresa(self):
        self.LimpaFrame(self.ct_config)
        self.DesativaBotao(self.fr_menuConfig, self.bt_confEmpresa)
        self.mainempresa(self.ct_config)

    # janela COnfiguração banco de dados
    def janelaDbConf(self):
        self.LimpaFrame(self.ct_config)
        self.DesativaBotao(self.fr_menuConfig, self.bt_confDB)
        self.maindbconf(self.ct_config)
