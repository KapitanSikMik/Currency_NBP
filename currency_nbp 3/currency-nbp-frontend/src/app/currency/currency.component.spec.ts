import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';
import { CurrencyComponent } from './currency.component';
import { CurrencyService } from '../currency.service';

describe('CurrencyComponent', () => {
  let component: CurrencyComponent;
  let fixture: ComponentFixture<CurrencyComponent>;
  let currencyService: CurrencyService;

  beforeEach(async () => {
    const currencyServiceMock = {
      getRates: jasmine.createSpy('getRates').and.returnValue(of({ data: [{ code: 'USD', rate: 1.2 }, { code: 'EUR', rate: 0.9 }] }))
    };

    await TestBed.configureTestingModule({
      declarations: [CurrencyComponent],
      providers: [
        { provide: CurrencyService, useValue: currencyServiceMock }
      ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CurrencyComponent);
    component = fixture.componentInstance;
    currencyService = TestBed.inject(CurrencyService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should fetch rates on getRates call', () => {
    component.getRates();
    expect(currencyService.getRates).toHaveBeenCalled();
    expect(component.rates.length).toBe(2);
    expect(component.showRates).toBeTrue();
  });
});