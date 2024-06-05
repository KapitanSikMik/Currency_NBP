import { Component, OnInit } from '@angular/core';
import { CurrencyService } from '../currency.service';

interface Rate {
  code: string;
  rate: number;
}

@Component({
  selector: 'app-currency',
  templateUrl: './currency.component.html',
  styleUrls: ['./currency.component.css']
})

export class CurrencyComponent implements OnInit {
  rates: Rate[] = [];
  showRates: boolean = false;

  constructor(private currencyService: CurrencyService) { }

  ngOnInit() { }

  getRates() {
    this.currencyService.getRates().subscribe(data => {
      this.rates = data.data;
      this.showRates = true;
    });
  }
}
