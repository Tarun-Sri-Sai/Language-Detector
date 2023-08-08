import { Component } from '@angular/core';
import { AppService } from '../app.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.css'],
})
export class InputComponent {
  textInput: string = '';
  private timeout: boolean = false;
  minCharacters: number = 20;
  private timeoutMillis: number = 100;

  constructor(private http: HttpClient, private app: AppService) {}

  detectLanguage(): void {
    if (this.timeout) {
      return;
    }

    this.timeout = true;

    if (!this.isValidLength()) {
      this.resetTimeout();
      return;
    }

    this.computeLanguage();
    this.resetTimeout();
  }

  computeLanguage(): void {
    this.http
      .post<any>('http://localhost:5000/language_detector/language', {
        text_input: this.textInput,
      })
      .subscribe({
        next: (response) => {
          this.app.result = response['language_code'];
        },
        error: (error) => {
          console.error("Couldn't compute language due to: ", error);
        },
      });
  }

  isValidLength(): boolean {
    return (
      this.textInput.trim().replaceAll(/\s+/g, ' ').length >= this.minCharacters
    );
  }

  resetTimeout(): void {
    setTimeout(() => {
      this.timeout = false;
    }, this.timeoutMillis);
  }
}
