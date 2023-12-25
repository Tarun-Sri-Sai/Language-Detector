import { Component } from '@angular/core';
import { LanguageService } from './language.service';

@Component({
  selector: 'app-input',
  template: `
    <h5 class="form-group">
      <label class="top-spacing" for="text"> Enter Text: </label>
      <textarea
        class="form-control top-spacing"
        id="text"
        [(ngModel)]="textInput"
        (input)="sendInput()"
      >
      </textarea>
    </h5>
    <div *ngIf="!isValidLength()" class="alert alert-warning">
      Please enter atleast {{ minCharacters }} characters
    </div>

  `,
  styles: [`

  `],
})
export class InputComponent {
  textInput: string = '';
  minCharacters: number = 20;

  constructor(private languageService: LanguageService) {}

  isValidLength(): boolean {
    return (
      this.textInput.trim().replaceAll(/\s+/g, ' ').length >= this.minCharacters
    );
  }

  sendInput(): void {
    if (!this.isValidLength()) {
      return;
    }
    this.languageService.detectLanguage(this.textInput);
  }
}

