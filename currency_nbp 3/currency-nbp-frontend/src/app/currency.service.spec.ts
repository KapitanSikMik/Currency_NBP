import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { CurrencyService } from './currency.service';

describe('CurrencyService', () => {
  let service: CurrencyService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [CurrencyService]
    });
    service = TestBed.inject(CurrencyService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should fetch rates successfully', () => {
    const mockRates = {
      data: [
        { code: 'USD', rate: 1.2 },
        { code: 'EUR', rate: 0.9 }
      ]
    };

    service.getRates().subscribe((rates) => {
      expect(rates).toEqual(mockRates);
    });

    const req = httpMock.expectOne('http://localhost:8000/api/get-rates/');
    expect(req.request.method).toBe('GET');
    req.flush(mockRates);
  });
});
