import { Component } from '@angular/core';
import { LanguageService } from '../language.service';

@Component({
    selector: 'app-input',
    templateUrl: './input.component.html',
    styleUrls: ['./input.component.css'],
})
export class InputComponent {
    textInput: string = '';
    minCharacters: number = 20;

    constructor(private languageService: LanguageService) {}

    isValidLength(): boolean {
        return (
            this.textInput.trim().replaceAll(/\s+/g, ' ').length >=
            this.minCharacters
        );
    }

    sendInput(): void {
        if (!this.isValidLength()) {
            return;
        }
        this.languageService.detectLanguage(this.textInput);
    }
}
